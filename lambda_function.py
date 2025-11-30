import json

def lambda_handler(event, context):
    S3_BUCKET_NAME = "aws-river-hawks"
    S3_REGION = "us-west-2"
    s3_base_url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com"

    river_hawk_logo_url = f"{s3_base_url}/2349.png"
    cloud_logo_url = "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"
    font_url = f"{s3_base_url}/roboto.ttf"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>River Hawk Cloud Deployment Week 6</title>

    <style>
        @font-face {{
            font-family: 'Roboto';
            src: url('{font_url}') format('truetype');
        }}

        body {{
            font-family: 'Roboto', sans-serif;
            background-color: #004990; /* UML Blue */
            color: white;
            text-align: center;
            padding-top: 60px;
        }}

        .header-logo {{
            display: block;
            margin: 0 auto;
            max-width: 260px;
            height: auto;
            margin-bottom: 40px;
        }}

        .cloud-logo {{
            height: 38px;
            vertical-align: middle;
            filter: brightness(0) invert(1);
            opacity: 0.9;
            margin: 0 8px;

            position: relative;
            top: 10px;
        }}

        .inline-msg {{
            font-size: 2em;
            font-weight: bold;
            margin-top: 20px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}
    </style>
</head>
<body>

    <img src="{river_hawk_logo_url}"
         alt="UMass Lowell River Hawks"
         class="header-logo">

    <div class="inline-msg">
        Served by
        <img src="{cloud_logo_url}" alt="AWS Logo" class="cloud-logo">
        Lambda
    </div>

</body>
</html>
"""

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_content
    }

