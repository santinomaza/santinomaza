terraform {
  cloud {
    organization = "hashicorps-codecamp"  # Replace with your actual org name
    workspaces {
      name = "example-project"  # Choose a workspace name
    }
  }
}

# Configure the AWS Provider (uses your CLI credentials automatically)
provider "aws" {
  region = "us-east-2"  # Change if needed (e.g., "us-west-1")
}

# Create an EC2 instance
resource "aws_instance" "codecamp_instance" {
  ami            = "ami-08962a4068733a2b6" # New AMI (Ubuntu 20.04)
  #ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 (us-east-2)
  instance_type = "t2.micro"               # Free-tier eligible
  tags = {
    Name = var.instance_name
  }
}

# Output the instance's public IP
#output "instance_public_ip" {
#  value = aws_instance.codecamp_instance.public_ip
#}
