### **Step-by-Step Guide to Fix Terraform Large File Commits**  
*(When you accidentally commit `.terraform/` and can’t push to GitHub)*  

---

### **1️⃣ Identify the Problem**  
Check if large files exist in your Git history:  
```bash
git log --stat | grep -E "\.terraform/|tfstate|large"
```  
- If you see large files (e.g., `680.27 MB`), proceed below.  

---

### **2️⃣ Remove Large Files Locally**  
Delete the cached Terraform files:  
```bash
rm -rf .terraform          # Delete local cache
git rm -r --cached .terraform  # Remove from Git tracking (if staged)
```

---

### **3️⃣ Update `.gitignore`**  
Ensure these lines exist in `.gitignore`:  
```bash
# Terraform files
.terraform/
*.tfstate
*.tfstate.backup
*.tfvars
```  
Add/update the file:  
```bash
echo -e "\n# Terraform\n.terraform/\n*.tfstate*" >> .gitignore
git add .gitignore
git commit -m "Update .gitignore"
```

---

### **4️⃣ Purge Large Files from Git History**  
Use `git filter-repo` (install via `brew install git-filter-repo`):  
```bash
git filter-repo --path .terraform/ --invert-paths --force
```  
**No `filter-repo`?** Use this alternative:  
```bash
git filter-branch --tree-filter 'rm -rf .terraform' --prune-empty HEAD
```

---

### **5️⃣ Force Push to GitHub**  
Overwrite remote history:  
```bash
git push origin main --force
```  
> ⚠️ **Warning**: This overwrites remote history. Ensure your team is synced.

---

### **6️⃣ Reinitialize Terraform**  
```bash
terraform init   # Recreates `.terraform/` locally (ignored by Git)
```

---

### **✅ Verify Success**  
- Check GitHub: Large files should be gone.  
- Confirm locally:  
  ```bash
  git status           # Should NOT show `.terraform/`
  ls .terraform/      # Folder exists locally but is untracked
  ```

---

### **Prevent Future Issues**  
1. **Always check** `git status` before committing.  
2. **Use remote state** (e.g., Terraform Cloud/AWS S3) for teams.  
3. **Never manually edit** `.terraform/` or `*.tfstate`.  

---

### **Troubleshooting**  
- **Still errors?** Try a fresh clone:  
  ```bash
  git clone git@github.com:your-repo.git fresh_copy
  cp -r old_repo/*.tf fresh_copy/
  ```
- **Need history?** Use `git lfs` for large files (not recommended for providers).  

This method **guarantees** your repo syncs with GitHub while keeping Terraform functional. 🚀