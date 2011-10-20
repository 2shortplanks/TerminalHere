import sublime, sublime_plugin, os
from subprocess import call

class TerminalHereCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		if self.view.is_scratch():
			sublime.error_message("Can't open a terminal for a scratch document")
			return

		# work out the directory.  Note we need to resolve the symbolic links
		# do that terminal doesn't freak out if we pass, say, "/etc"
		directory = os.path.realpath( os.path.dirname( self.view.file_name() ));
		
		# yey, this works on 10.7
		call(["open","-a","Terminal", directory])

