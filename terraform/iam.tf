resource "aws_iam_openid_connect_provider" "this" {
  url = var.oidc.url

  client_id_list = var.oidc.audience

  thumbprint_list = var.oidc.thumbprint_list

  tags = {
    IAC = "True",
  }
}

resource "aws_iam_role" "this" {
  name = "ecr_role"

  assume_role_policy = jsonencode({
    Version : "2012-10-17",
    Statement : [
      {
        Effect : "Allow",
        Action : "sts:AssumeRoleWithWebIdentity",
        Principal : {
          Federated : var.oidc.federated_arn
        },
        Condition : {
          StringEquals : {
            "${var.oidc.audience_key}" : var.oidc.audience,
            "${var.oidc.subject_key}" : var.oidc.subject
          }
        }
      }
    ]
  })

  inline_policy {
    name = "ecr-app-permission"
    policy = jsonencode({
      Version : "2012-10-17",
      Statement : [
        {
          Effect : "Allow",
          Action : [
            "ecr:GetAuthorizationToken",
            "ecr:BatchCheckLayerAvailability",
            "ecr:GetDownloadUrlForLayer",
            "ecr:BatchGetImage",
            "ecr:InitiateLayerUpload",
            "ecr:UploadLayerPart",
            "ecr:CompleteLayerUpload",
            "ecr:PutImage"
          ],
          Resource : "*"
        }
      ]
    })
  }

  tags = {
    IAC = "true"
  }
}
