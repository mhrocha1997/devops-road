variable "aws_profile" {
  type = string
}

variable "aws_region" {
  type = string
}


variable "oidc" {
  type = object({
    federated_arn   = string
    audience        = list(string)
    subject         = list(string)
    audience_key    = string
    subject_key     = string
    thumbprint_list = list(string)
    url             = string
  })
}

variable "ecr" {
  type = object({
    name = string
  })
}