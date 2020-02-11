# tree_generator.py

Works only for python 3

Output:
```

$bash: python3 tree_generator.py -m http -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/
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
