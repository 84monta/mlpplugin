# ChatGPT LP plugins


## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! 
You can solve "SIMPLE" Linear programming.

## Tips for running with WSL

Add Portforwading Setting
```cmd
netsh interface portproxy add v4tov4 listenport=5003 listenaddr=127.0.0.1 connectport=5003 connectaddress=<<YOUR WSL IP>>
```

Delete Portfowarding Setting
```cmd
netsh interface portproxy delete v4tov4 listenport=5003 listenaddr=127.0.0.1
```

Check Portfowarding Setting
```cmd
netsh interface portproxy show all
```

#FAQ
Q1: Something wrong...
A1: Yes...(This may be resolved by upgrading the ChatGPT version)

Q2:The formulation is wrong.
A2:Set up a more detailed problem set.