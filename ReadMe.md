# tree_generator.py

python3-class-viewer is a command line utility which examines all classes and their members for specified modules.

Get started with:

```
$bash: python3 tree_generator.py -h
```


Output:
```

$bash: python3 tree_generator.py -m http 
		C: http.client.BadStatusLine [ http.client.BadStatusLine , http.client.HTTPException , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: http.client.CannotSendHeader [ http.client.CannotSendHeader , http.client.ImproperConnectionState , http.client.HTTPException , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: http.client.CannotSendRequest [ http.client.CannotSendRequest , http.client.ImproperConnectionState , http.client.HTTPException , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: http.client.HTTPConnection [ http.client.HTTPConnection , builtins.object]
			P: auto_open 1
			P: debuglevel 0
			P: default_port 80
			P: response_class <class 'http.client.HTTPResponse'>
			F: close(self)
			F: connect(self)
			F: endheaders(self,message_body,encode_chunked)
			F: getresponse(self)
			F: putheader(self,header,values)
			F: putrequest(self,method,url,skip_host,skip_accept_encoding)
			F: request(self,method,url,body,headers,encode_chunked)
			F: send(self,data)
			F: set_debuglevel(self,level)
	

```

# Disclaimer:
This tool was developed as part of a Hackfest event at veracode, with hope to be useful for accelerating research work. Its more under development with more stability with active usage within team. Not accepting any PR/bug reports at the moment. All work done as part of this is a personal project, so direct all complaints to me.

# LICENSE:

TreeViewer is released under the [MIT license](https://opensource.org/licenses/MIT)

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
