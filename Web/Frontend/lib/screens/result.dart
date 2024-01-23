import 'package:flutter/material.dart';
import 'package:tave/screens/webpage.dart';
import 'package:tave/controller/functions.dart';
import 'dart:typed_data';  // Uint8List 사용을 위한 import

class ResultPage extends StatelessWidget {
  final String webtoonTitle;
  final Map<String, dynamic> characterInfo;

  ResultPage({
    required this.webtoonTitle,
    required this.characterInfo,
  });

  @override
  Widget build(BuildContext context) {
    // characterInfo에서 이미지 URL을 가져옵니다.
    Uint8List imageBytes = characterInfo['image_data'];

    TextStyle fontStyle1 = TextStyle(
      fontFamily: 'Yeongdeok Snow Crab',
      fontSize: 20,
    );

    TextStyle fontStyle2 = TextStyle(
      fontFamily: 'Yeongdeok Sea',
      fontSize: 20,
    );

    Color backgroundColor = Color.fromRGBO(102, 255, 102, 0.4);

    return Scaffold(
      backgroundColor: backgroundColor,
      appBar: AppBar(
        toolbarHeight: 80,
        backgroundColor: backgroundColor,
        title: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Text(
              'Hello 캐릭 TO 리얼 World !',
              style: fontStyle2.copyWith(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              '여러분이 원하는 웹툰의 정보로 배우를 추천해줘요!',
              style: fontStyle2,
            ),
          ],
        ),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Image.memory(
              imageBytes, // characterInfo에서 가져온 Uint8List 형태의 이미지 데이터 사용
              height: 500,
              width: 500,
              fit: BoxFit.cover,
            ),
            SizedBox(height: 20),
            Text(
              'Selected Text: ${webtoonTitle}', // webtoonTitle을 표시합니다.
              style: TextStyle(fontSize: 20),
            ),
          ],
        ),
      ),
    );
  }
}