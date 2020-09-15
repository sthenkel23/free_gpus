# Get free GPU

1. Store utils/helpers.py in your google drive folder (at /content/drive)
2. Run utils/ssh-connect.ipynb as google colaboratory (ensure the session is GPU/TPU)
3. Use printed info to connect using ssh
    3.1. I started using vs code for ease. In case you wanna follow this approach, follow next step(s)
4. Install extension called RemoteSSH
4.1 RemoteSSH > Select SSH configuration file
4.2 Open config file (e.g. Users/shenkel/.ssh/config) and insert info from 3. 
4.3 Connect with RemoteSSH connection, insert password and let the fun begin. Start at /content/drive/My Drive/workspaces/MyWorkspace and create or pull git or whatever


## Additional comments:
- Google colab session needs to be kept active and ssh config info changes and needs to be filled by hand per session