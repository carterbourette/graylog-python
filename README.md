# Python-Graylog

A sample application using Graylog.

> Built to open standards, Graylog’s connectivity and interoperability seamlessly collects, enhances, stores, and analyzes log data.
– [Graylog](https://www.graylog.org/products/open-source) 

So we could hook Graylog into the standard logging library in Python, but we're going to adhere to [The 12 Factor App](https://12factor.net/logs) as our guiding principle.

> A twelve-factor app never concerns itself with routing or storage of its output stream. It should not attempt to write to or manage logfiles. Instead, each running process writes its event stream, unbuffered, to stdout. During local development, the developer will view this stream in the foreground of their terminal to observe the app’s behavior.

Enter, the [`logging driver`](https://www.docker.com/blog/adventures-in-gelf/#h.ipgypyjrkmws)


## Getting Started

It's as easy as:

    $ docker-compose up -d

You can find the Graylog UI at: http://localhost:9000

Navigate to the Graylog UI, under the `System/Inputs` directory create an input `GELF UDP` then create an extractor on the message field `JSON`.

TODO: Automate Input & Extractor creation.


## Resources

* Product: https://www.graylog.org/products/open-source
* Docker Setup: https://docs.graylog.org/en/3.3/pages/installation/docker.html
* Docs Planning: https://docs.graylog.org/en/3.3/pages/getting_started/planning.html
* Automating Setup: https://stackoverflow.com/a/40636190
* Logging: https://www.docker.com/blog/adventures-in-gelf/#h.ipgypyjrkmws
