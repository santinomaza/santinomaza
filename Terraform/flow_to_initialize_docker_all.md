Here's a complete **step-by-step guide** from starting VirtualBox to destroying resources, with verification at each stage:

---

### **1. Start VirtualBox & Docker Machine**
```bash
# Start VirtualBox VM (if not running)
docker-machine start default

# Initialize Docker environment
eval $(docker-machine env default)
```

**Verify:**
```bash
docker-machine ls
```
✅ Should show `default` with **STATE = "Running"**

---

### **2. Check Docker Connectivity**
```bash
docker ps
```
✅ Should show containers (empty list is OK)  
❌ If error, run `eval $(docker-machine env default)` again

---

### **3. Create Terraform Project**
```bash
mkdir learn-terraform-docker-container
cd learn-terraform-docker-container
```

---

### **4. Create `main.tf`**
```bash
cat > main.tf <<EOF
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host     = "tcp://$(docker-machine ip default):2376"
  cert_path = "/Users/$(whoami)/.docker/machine/machines/default"
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}
EOF
```

**Verify:**
```bash
cat main.tf
```
✅ Check if `provider "docker"` has your correct IP and cert path

---

### **5. Initialize Terraform**
```bash
terraform init
```
✅ Should see:  
*"Terraform has been successfully initialized!"*

---

### **6. Deploy NGINX Container**
```bash
terraform apply
```
Type `yes` when prompted.  
✅ Should see:  
*"Apply complete! Resources: 2 added"*

---

### **7. Verify Resources**
```bash
# Check container
docker ps | grep tutorial

# Check image
docker images | grep nginx

# Access NGINX (replace IP if different)
curl -I http://$(docker-machine ip default):8000
```
✅ Should return HTTP 200 OK

---

### **8. Clean Up**
```bash
terraform destroy
```
Type `yes` when prompted.  
✅ Should see:  
*"Destroy complete! Resources: 2 destroyed."*

**Final Verification:**
```bash
docker ps -a | grep tutorial  # Should show no containers
docker images | grep nginx    # Image removed (keep_locally=false)
```

---

### **9. Stop Docker Machine (Optional)**
```bash
docker-machine stop default
```

---

### **Troubleshooting Cheatsheet**
| Issue | Solution |
|-------|----------|
| `Connection refused` | Run `eval $(docker-machine env default)` |
| `TLS handshake timeout` | `docker-machine regenerate-certs default` |
| Port 8000 not working | Check `docker-machine ip default` matches browser URL |
| `certificate signed by unknown authority` | Verify `cert_path` in `main.tf` |

---

### **Visual Workflow**
```
Start VirtualBox → Initialize Docker → Terraform Init → Apply → Verify → Destroy
```

Let me know if you'd like to explore more complex setups! 🐳