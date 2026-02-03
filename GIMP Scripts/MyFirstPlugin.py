# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 07:05:00 2026

@author: sucre
"""
import sys
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GimpUi, GLib

class MyFirstPlugin (Gimp.PlugIn):
    def do_query_procedures(self):
        return [ "jb-plug-in-first-try" ]
    
    def do_set_i18n (self, name):
        return False
    
    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)
        
        procedure.set_image_types("*")
        
        procedure.set_menu_label("My first Python plug-in")
        procedure.add_menu_path('<Image>/Filters/Tutorial/')
        
        procedure.set_documentation("My first Python plug-in tryout",
                                    "My first Python 3 plug-in for GIMP 3",
                                    name)
        procedure.set_attribution("Your name", "Your name", "2023")
    
        return procedure
    
    def run(self, procedure, run_mode, image, drawables, config, run_data):
        Gimp.message("Hello world!")
        # do what you want to do, then, in case of success, return:
        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())