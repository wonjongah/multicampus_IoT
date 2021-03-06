// 단항연산자로 쓰일 때
// -() 부호를 바꿔라
// typeof 어떤 데이터 타입인가 검사해서 문자열로 출력해라

console.log(typeof 52);
console.log(typeof(typeof 52));
// typeof가 리턴하는 것은 문자열이다

console.log(typeof 1 + "문자열");

// 단항 연산자가 우선순위가 높냐 이항 연산자가 우선순위가 높냐
// 이항이 높으면 1 + 문자열의 데이터 값이 어떻게 되냐? 문자열...
// 그런데 단항 높으면 1의 타입오브 먼저 한다, 넘버 + 문자열
// 해보면 단항연산자가 우선순위 높다