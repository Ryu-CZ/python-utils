'''
@summary: This module contains methods to translate strings between various naming conventions.

Created on 5 Feb 2015

@author: thandeus@gmail.com
'''
import re

camelSplitPattern = re.compile('([a-z]+)|([A-Z][a-z]+)|([0-9]+)')

#------------------------------------------------------------------------------ 
#Text formating features
#------------------------------------------------------------------------------ 

def toHighCamelCase(snake_str):
    """! Translates string from snake_case to HighCamelCase
    @param snake_str: string in snake_case f.e.: 'input_text'
    @type snake_str: str
    @return: equivalent of snake_case in HighCamelCase f.e.: 'InputText'
    @rtype: str"""
    components = snake_str.split('_')
    return "".join(x.title() for x in components)

def toLowCamelCase(snake_str):
    """! Translates string from snake_case to lowCamelCase
    @param snake_str: string in snake_case f.e.: 'input_text'
    @type snake_str: str
    @return: equivalent of snake_case in lowCamelCase f.e.: 'inputText'
    @rtype: str"""
    components = snake_str.split('_')
    # Capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])

def toSnakeCase(camelStr):
    """! Translates string from camelCase(high or low) to snake_case
    @param camelStr: string in camelCase f.e.: 'inputText' also 'InputText'
    @type camelStr: str
    @return: equivalent of camelStr in snake_case f.e.: 'input_text'
    @rtype: str"""
    return '_'.join((word.group(0) for word in camelSplitPattern.finditer(camelStr))).lower()

