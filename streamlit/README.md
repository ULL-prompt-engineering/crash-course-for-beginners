Working with Streamlit is simple. First you sprinkle a few Streamlit commands into a normal Python script, then you run it with streamlit run:

```
streamlit run your_script.py [-- script args]
```

As soon as you run the script as shown above, a local Streamlit server will spin up and your app will open in a new tab in your default web browser. The app is your canvas, where you'll draw charts, text, widgets, tables, and more.

What gets drawn in the app is up to you. For example `st.text` writes raw text to your app, and `st.line_chart` draws a line chart. 

Another way of running Streamlit is to run it as a Python module. This can be useful when configuring an IDE like PyCharm to work with Streamlit:

```
python -m streamlit run your_script.py
```

## Execution

```
(.venv) ➜  crash-course-for-beginners git:(main) ✗ streamlit run hello-streamlit.py

      👋 Welcome to Streamlit!

      If you’d like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:  

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.209.2.80:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
```

## References

* https://streamlit.io/