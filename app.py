#!/usr/bin/env python3

from aws_cdk import core
from aws_static_website.website_stack import WebsiteStack

project_name = "aws-static-website"
parameters = {
    "bucket_name" : "bucket.domain.name",
    "aliases" : ["bucket.domain.name"],
    "hosted_zone_id" : "",
    "acm_certificate_arn" : "",
}

app = core.App()
WebsiteStack(app, 
    id=project_name,
    params=parameters
)

app.synth()
