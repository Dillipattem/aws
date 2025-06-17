import boto3
import csv
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Get bucket and object key from event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    # Define destination bucket
    destination_bucket = 'processed-55'  # Replace with your actual bucket name

    try:
        # Get the CSV file from S3
        response = s3.get_object(Bucket=source_bucket, Key=source_key)
        raw_data = response['Body'].read().decode('utf-8')

        # Read CSV content
        input_stream = io.StringIO(raw_data)
        reader = csv.DictReader(input_stream)
        cleaned_rows = [row for row in reader if all(row.values())]

        # Prepare cleaned CSV output
        output_stream = io.StringIO()
        writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

        # Upload cleaned file to destination S3 bucket
        cleaned_key = f"cleaned_{source_key}"
        s3.put_object(
            Bucket=destination_bucket,
            Key=cleaned_key,
            Body=output_stream.getvalue().encode('utf-8')
        )

        return {
            'statusCode': 200,
            'body': f"Successfully cleaned and saved as {cleaned_key}"
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': f"Error processing file: {str(e)}"
        }

