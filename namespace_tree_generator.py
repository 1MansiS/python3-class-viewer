import pkgutil
import importlib
import sys,os
from traceback import print_tb
import inspect
from optparse import OptionParser

class TreeGenerator:

	MODULE = ''
	SUB_MODULE = ''

	def explore_module(self, module_name):
		m = importlib.import_module(module_name)

		for name, data in inspect.getmembers(m,inspect.isclass):
			if name.startswith('__') and name != '__init__':
				continue
			# Without this check, it was giving information about all import classes as well.
			elif inspect.getmodule(data).__name__ != module_name:
				continue
			else:
				# Print class name and its inheritance. Note: getmro, will get just immediate inherited super class and not entire heirarchy
				print("\t\tC:",module_name+"."+name, "[" , ' , '.join('{}'.format(inherited_class_name.__module__ + '.' + inherited_class_name.__name__) for inherited_class_name in inspect.getmro(data)) + "]" )
				# If its not a routine, it should be a property
				for prop, prop_data in inspect.getmembers(data,lambda a:not(inspect.isroutine(a))):
					if not prop.strip().startswith('_') and not prop.strip().endswith('_'):
						print("\t\t\tP:",prop, prop_data)	
				for method, method_data in inspect.getmembers(data,inspect.ismethod):
					if not method.strip().startswith('_') or method.strip() == '__init__':
						print("\t\t\tM:" , method.strip() + "(" + ','.join('{}'.format(key.strip()) for key, _ in inspect.signature(method_data).parameters.items()).strip() + ")" )
				for func, func_data in inspect.getmembers(data,inspect.isfunction):
					if not func.strip().startswith('_') or func.strip()  == '__init__':
						print("\t\t\tF:",func.strip()+ "(" + ','.join('{}'.format(key.strip()) for key, _ in inspect.signature(func_data).parameters.items()).strip() + ")" )


	def explore_package(self, module_name):
			for p in sys.path:
				print("Path " , p)

			self.explore_module(module_name)
			m = importlib.util.find_spec(module_name)

			#print("Importing path" + type(m))

			#for loader, sub_module , ispkg in pkgutil.walk_packages(path=sys.path):

			for loader, sub_module , ispkg in pkgutil.walk_packages(path=m.submodule_search_locations):
				try: 
					importlib.import_module(module_name+"."+sub_module)
					# If its a package we would need to re-explore it till all sub-packages are also evaluated
					if(ispkg == True):
						print("Is package",module_name+"."+sub_module,loader)
						self.explore_package(module_name+"."+sub_module)
					# Its not a package, so should be a module
					else:
						print(module_name+"."+sub_module)
						self.explore_module(module_name+"."+sub_module)

				except:
					#type, value, traceback = sys.exc_info()
					#print_tb(traceback)
					print("Unexpected error:", sys.exc_info()[0], module_name+'.'+sub_module)
					#pass
					continue

		# For Django, since we not running thru command line using manage.py, we would need to explicitly initialize it
		#sys.path.insert(0, "/Users/msheth/Documents/Research-Projects/Python-Django2/testcases/django2-simpleapp/") 
		#sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/")
		#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simpleapp.settings")

	def parse_command_line(self):
		parser = OptionParser()

		parser.add_option("--module" , "-m" , action="store" , type="string" , dest="module" , help = "List all classes/functions/methods within this module.")
		parser.add_option("--sub_modules" , "-s" , action="store" , type="string" , dest="sub_module" , help = "find all submodules within this module.")


		(options, args) = parser.parse_args()
		sys.path.insert(0,options.sub_module)
		#sys.meta_path.append(options.sub_module)	
		self.MODULE = options.module
		self.SUB_MODULE = options.sub_module
		
	def main(self):
		self.parse_command_line()
		self.explore_package(self.MODULE)

if __name__ == "__main__":
	tree_generator = TreeGenerator()
	tree_generator.main()
