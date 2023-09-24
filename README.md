Installation command:

```
bash <(curl -s0 https://raw.githubusercontent.com/leenperjasknegt/mpjpegcloudurl/main/install.sh)
```

If you get the following error: Command 'curl' not found

```
sudo apt install curl
```

If you want to change some settings after installation:

```
python3 /opt/nxurl/url.py
```

IMPORTANT!
Make sure Digest authentication is activated for the user account you use.
Go to users > Management > choose the user (or creat a new one) and click edit 
Click on the three dots on the bottem left corner and enable Digest authentication
