# model_deplyoment_azure_function

```
func init regression_model --python
```
This will generate `regression_model` dir with `local.settings.json`, `host.json`,`requirements.txt`, `getting_started.md` and a `.vscode` dir (with a `extensions.json`) in the main dir(that includes api dir and requrements.txt).
```
cd titanic_model
```
With `func new`, Select `HTTP trigger` and a function name. a dir with the specified function name will be created with a `__init__.py` and a `function.json`. Put the function code in `__init__.py`.

The following sets up local debugging environment.
```
# windows/linux/mac intel chip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# work around for mac m1 machines
conda create --name py39 python=3.9
conda activate py39
pip install -r requirements.txt
```


start local debugging
```
func host start
python api_test.py
```

Test function in cloud 


```
az login
func azure functionapp publish titanicmodeltest --build remote
```
Get endpoint url in azure portal and test out inference
```
python api_test.py
```


Trouble shooting:
if you meet ssl certification error, then use the foolowing command to install certification:
```
open /Applications/"Python 3.11"/"Install Certificates.command"
```

Local testing api
```
python api_test.py
```


