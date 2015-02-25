# flask-tumblelog
following a tutorial for Tumblelog Application with Flask and MongoEngine from mongodb.org

^irtualenv                                     
|                                              
+->tumblelog system                            
    +-->__init__.py                            
        manage.py                              
        models.py                              
        views.py  +---> templates+>posts       
        admin.py                 |->base.html  
        auth.py                  |->list.html  
                                 +-^detail.html
                                 |             
                                 +>admin       
                                  +>base.html  
                                  |>list.html  
                                  +^detail.html

