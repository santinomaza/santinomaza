Here's a complete step-by-step guide covering AWS CLI installation, IAM user creation, security best practices, and Terraform workflow:

---

### **Step 1: Install AWS CLI**
#### **On macOS/Linux:**
```bash
# Download and install AWS CLI v2
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Verify installation
aws --version
```

#### **On Windows:**
1. Download the [AWS CLI MSI installer](https://awscli.amazonaws.com/AWSCLI2.msi)
2. Run the installer as Administrator
3. Open Command Prompt and verify:
   ```cmd
   aws --version
   ```

---

### **Step 2: Create an IAM User (Avoid Root Credentials)**
1. **Go to [IAM Console](https://console.aws.amazon.com/iam)**
2. **Users** → **Add user**
   - Name: `terraform-user`
   - Select **Programmatic access** (uncheck console access)
3. **Set permissions**:
   - Attach policy: `AdministratorAccess` *(for learning only)*
4. **Create user** → **Download .csv** (contains `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY`)

---

### **Step 3: Configure AWS CLI Securely**
```bash
aws configure
```
Enter:
- `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY` (from the .csv)
- Default region: `us-east-2`
- Output format: `json`

**Security Tip**:  
- Never share/commit these keys.
- Rotate keys every 90 days.

---

### **Step 4: Terraform Setup**
#### **1. Create `main.tf`**
```hcl
provider "aws" {
  region = "us-east-2"  # Matches CLI config
}

resource "aws_instance" "codecamp_instance" {
  ami           = "ami-08962a4068733a2b6"  # Ubuntu 20.04 (us-east-2)
  instance_type = "t2.micro"               # Free-tier eligible
  tags = {
    Name = "CodeCamp-Instance"
  }
}

output "instance_public_ip" {
  value = aws_instance.codecamp_instance.public_ip
}
```

#### **2. Initialize & Apply**
```bash
terraform init    # Downloads providers
terraform plan   # Preview changes
terraform apply  # Type "yes" to create (costs may apply)
```

#### **3. Verify**
- Check EC2 console:  
  [EC2 Instances](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:)
- Or use CLI:
  ```bash
  aws ec2 describe-instances \
    --query "Reservations[].Instances[?Tags[?Value=='CodeCamp-Instance']].PublicIpAddress" \
    --output text
  ```

---

### **Step 5: Clean Up (Avoid Ongoing Charges)**
```bash
terraform destroy  # Deletes all created resources
```

**Post-Destroy**:
1. **Delete IAM User** (if no longer needed):
   - IAM Console → Users → Delete `terraform-user`
2. **Rotate Credentials** (if reusing user):
   - IAM → Users → Security credentials → Delete old access key

---

### **Security Risks & Mitigations**
| Risk | Solution |
|------|----------|
| **Exposed Credentials** | Never commit `.csv`/`~/.aws/credentials` to Git |
| **Over-Permissioned User** | Replace `AdministratorAccess` with [least-privilege policy](https://awspolicygen.s3.amazonaws.com/policygen.html) |
| **Forgotten Resources** | Always `terraform destroy` after labs |
| **Free Tier Overuse** | Monitor at [AWS Free Tier Usage](https://console.aws.amazon.com/billing/home#/freetier) |

---

### **Cost-Saving Tips**
- Use `t4g.micro` (ARM) instead of `t2.micro` post-Free Tier (~40% cheaper)
- Enable **billing alerts**:
  ```bash
  aws budgets create-budget --budget file://budget.json
  ```
  ([Example budget.json](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html))

---

### **Need Help?**
- To find AMIs for other regions:  
  ```bash
  aws ec2 describe-images --owners 099720109477 \
    --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" \
    --query 'sort_by(Images,&CreationDate)[-1].ImageId' \
    --output text
  ```
- For least-privilege policies: Ask for examples!

# Track costs
aws budgets create-budget --budget file://budget.json

# Find Ubuntu AMIs
aws ec2 describe-images --owners 099720109477 --filters "Name=name,Values=ubuntu*20.04*"

# Clean up everything
terraform destroy