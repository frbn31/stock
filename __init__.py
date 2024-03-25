from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


routers = []

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    new_routers = getattr(module, "routers", None)
    if new_routers:
        routers = routers + new_routers
globals()["routers"] = routers



models = []

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    new_models = getattr(module, "models", None)
    if new_models:
        models = models + new_models
globals()["models"] = models

# package_dir = Path(__file__).resolve().parent
#
#
# def recursive_route_include(package_dir, traversed_modules = [__name__]):
#     for (_, module_name, _) in iter_modules([package_dir]):
#         current_traversed_modules = traversed_modules + [module_name]
#         if ".".join(current_traversed_modules) == "framework.apps.base.routes.cloud":
#             module = import_module(".".join(current_traversed_modules))
#             print("")
#             
#             recursive_route_include(Path(module.__file__).resolve().parent, traversed_modules=list(current_traversed_modules))
#             router = getattr(module, "router", None)
#             if router:
#                 routers.append(router)
#         try:
#             module = import_module(".".join(current_traversed_modules))
#             recursive_route_include(Path(module.__file__).resolve().parent, traversed_modules=list(current_traversed_modules))
#             router = getattr(module, "router", None)
#             if router:
#                 routers.append(router)
#         except:
#             print(f"{'.'.join(current_traversed_modules)}: bruh")
#
# def recursive_table_model_include(package_dir, traversed_modules = [__name__]):
#     for (_, module_name, _) in iter_modules([package_dir]):
#         current_traversed_modules = traversed_modules + [module_name]
#         if "apps" in current_traversed_modules:
#             try:
#                 module = import_module(".".join(current_traversed_modules))
#                 recursive_table_model_include(Path(module.__file__).resolve().parent, traversed_modules=list(current_traversed_modules))
#                 for attribute_name in dir(module):
#                     potential_table_model = getattr(module, attribute_name)
#                     if isclass(potential_table_model):
#                         table_config = getattr(potential_table_model, "model_config", {})
#                         if table_config and (table_config.get("table", False) or False):
#                             table_models.append(potential_table_model) 
#             except:
#                 pass
#
# routers = []
# recursive_route_include(package_dir)
# globals()["routers"] = routers
#
# table_models = []
# recursive_table_model_include(package_dir)
# globals()["table_models"] = table_models

# package_dir = Path(__file__).resolve().parent
# for (_, module_name, _) in iter_modules([package_dir]):
#     if "apps" in module_name:
#         module = import_module(f"{__name__}.{module_name}")
#         for attribute_name in dir(module):
#             potential_table_model = getattr(module, attribute_name)
#             if isclass(potential_table_model):
#                 table_config = getattr(potential_table_model, "model_config", {})
#                 if table_config and (table_config.get("table", False) or False):
#                     table_models.append(potential_table_model) 
