# lykkex

Simple python wrapper for the [Lykke Exchange API](https://hft-service-dev.lykkex.net/swagger/ui/index.html). 

**Note** that the default environment is the development api of Lykkex. In production code, run 
```python
import lykkex
lykkex.set_api_environment("prod")
```
before making any api calls.

# Install

To install 
```
pip install .
```

# Run tests

```
python setup.py test
```