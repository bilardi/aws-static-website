#!/usr/bin/env python3

from aws_cdk import core
from aws_static_website.website_stack import WebsiteStack

project_name = "aws-static-website"
website_params = {
    "index_document": "index.html",
    "error_document": "index.html"
}
# hosted_params = {
#     "zone_name": "domain.name",
#     "zone_id": "Z23ABC4XYZL05B"
# }

app = core.App()
WebsiteStack(app, 
    id=project_name,
    bucket_name="bucket.domain.name",
    website_params=website_params,
    # hosted_params=hosted_params
)

app.synth()
