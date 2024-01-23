import 'package:flutter/material.dart';
import 'screens/webpage.dart';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  MyApp({Key?key}) : super(key:key);

  //This widet is the root of your application
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'title',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: WebPage(),
    );
  }
}
