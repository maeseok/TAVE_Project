import 'package:http/http.dart' as http;
import 'dart:convert';

  class WebtoonService {
  final String serverIP; // 서버의 IP 주소나 도메인을 저장할 변수

  WebtoonService(this.serverIP);

  // FastAPI 서버로부터 웹툰 캐릭터 목록을 가져오는 함수
  Future<List<String>> fetchCharacters(String webtoonTitle) async {
  final response = await http.post(
  Uri.parse('$serverIP/characters'),
  headers: {"Content-Type": "application/json"},
  body: json.encode({'title': webtoonTitle}),
  );

  if (response.statusCode == 200) {
  List<dynamic> characters = json.decode(response.body);
  return characters.cast<String>();
  } else {
  throw Exception('Failed to load characters');
  }
  }

  // FastAPI 서버에 선택된 웹툰 주연에 대한 정보 요청
  Future<Map<String, dynamic>> fetchCharacterInfo(String characterName) async {
    final response = await http.get(
      Uri.parse('$serverIP/characters/info?name=$characterName'),
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load character info');
    }
  }
}