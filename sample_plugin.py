from plugify.plugin import Plugin
# from plugify.pps import (s2sdk as s2) # s2sdk is a name of plugin to load from as syntetic module

class ExamplePlugin(Plugin):
	def plugin_start(self):
		print('ExamplePlugin::plugin_start')

    #def plugin_update(self, dt: float):
	#	print('ExamplePlugin::plugin_update')

	def plugin_end(self):
		print('ExamplePlugin::plugin_end')


def make_print(count: int, message: str):
    for _ in range(count):
        print(message)