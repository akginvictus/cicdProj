# Deployment Verification Checklist

## ✅ Pre-Deployment Checks
- [ ] GitHub workflow file is committed and pushed
- [ ] Azure Deployment Center is configured:
  - [ ] Registry server URL: `index.docker.io`
  - [ ] Image and tag: `akginvictus/devops:latest`
  - [ ] Port: `8000`
- [ ] Application setting `WEBSITES_PORT=8000` is set in Azure

## ✅ Post-Deployment Verification

### 1. GitHub Actions
- [ ] Go to: https://github.com/akginvictus/cicdProj/actions
- [ ] Latest workflow run shows ✅ (green checkmark)
- [ ] Both `build` and `deploy` jobs completed successfully
- [ ] Check deploy job logs for "Deploy to Azure Web App" success

### 2. Azure Portal
- [ ] Go to: https://portal.azure.com → `akgepita`
- [ ] Status shows "Running"
- [ ] Check Deployment Center → Logs for deployment activity
- [ ] Check Log stream for Flask/Python logs (not nginx)

### 3. Website Verification
- [ ] Visit: https://akgepita.azurewebsites.net
- [ ] Should show Flask app homepage (not nginx welcome page)
- [ ] Visit: https://akgepita.azurewebsites.net/about
- [ ] Should show "Aakash DevOps Project" page

## 🔧 If Still Seeing Nginx:
1. Verify container config in Deployment Center
2. Restart the Web App
3. Check logs for errors
4. Verify Docker image exists: https://hub.docker.com/r/akginvictus/devops/tags

