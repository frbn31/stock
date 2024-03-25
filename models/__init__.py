from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
from inspect import isclass

models = []

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        potential_table_model = getattr(module, attribute_name, None)
        if isclass(potential_table_model):
            table_config = getattr(potential_table_model, "model_config", {})
            if table_config and (table_config.get("table", False) or False):
                models.append(potential_table_model) 
globals()["models"] = models
