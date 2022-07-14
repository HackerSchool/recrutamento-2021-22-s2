import 'dart:html';

import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

//todo: add a money emoji, add money symbol


void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: 'Expenses Tracker',
      theme: ThemeData(scaffoldBackgroundColor: Colors.grey[200],),
      routes: {
        '/': (context) => WelcomePage(),
        '/HomePage' : (context) => HomePage(),
      },
      initialRoute: '/',
    );
  }
}

class WelcomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    return Scaffold(
        backgroundColor: Colors.grey[200],
        body: Column(
          children: [
            Padding(
              padding: EdgeInsets.all(250), //todo: arranjar forma de ficar no meio
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Center(child:
                  Text('Expenses Tracker',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 30,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  ),
                ],
              ),
            ),
            Padding(
              padding: EdgeInsets.only(left: 870, bottom: 10),
              child: GestureDetector(
                onTap: (){
                  Navigator.of(context).pushNamed('/HomePage');
                },
                child: Icon(Icons.arrow_forward_ios_sharp),
              ),
            )
          ],
        )
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: Text('Transactions',
          style: TextStyle(
            color: Colors.black,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          ),
        ),
        backgroundColor: Colors.white,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          UniversityExpenses(),
          HealthExpenses(),
          SupermarketExpenses(),
        ],
      ),
    );
  }
}


// ---------------------- Saving Expenses ---------------------

class saveHealthExpenses {
  late final int health;

  saveHealthExpenses({  required this.health});
}

class saveUniversityExpenses {
  late final int uni;

  saveUniversityExpenses({  required this.uni});
}

class saveSupermarketExpenses {
  late final int supermarket;

  saveSupermarketExpenses({  required this.supermarket});
}

// ---------------------- Expenses ----------------------------

class SupermarketExpenses extends StatefulWidget {
  @override
  _SupermarketExpenses createState() => _SupermarketExpenses();
}

class _SupermarketExpenses extends State<SupermarketExpenses> {
  int _counter = 0;
  late TextEditingController controller;
  int valueExpense = 0;

  void incrementCounter(int value) async{
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('counter') ?? 0) + value;
      prefs.setInt('counter', _counter);
    });
  }

  void _loadCounter() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('counter') ?? 0);
    });
  }

  @override
  void initState(){
    super.initState();
    controller = TextEditingController();
    _loadCounter();
  }

  @override
  void dispose(){
    controller.dispose();
    super.dispose();
  }

  void submit(){
    Navigator.of(context).pop(controller.text);

    controller.clear();
  }


  Future openDialog() => showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Add value expense'),
        content: TextField(
          autofocus: true,
          decoration: InputDecoration(hintText: 'Add the expense'),
          keyboardType: TextInputType.number,
          controller: controller,
        ),
        actions: [
          TextButton(
              onPressed: submit,
              child: Text('Done')
          )
        ],
      )
  );

  @override
  Widget build(BuildContext context){
    return Container(
      height: 50,
      margin: EdgeInsets.only(right: 200, left: 200),
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black26,
        ),
        borderRadius: BorderRadius.all(Radius.circular(20)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
              padding: EdgeInsets.all(10),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Icon(Icons.shopping_cart),
                  Text('Supermarket',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 20,
                    ),
                  ),
                  Text('$_counter',
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 20,
                      )
                  ),
                  GestureDetector(
                    onTap: () async {
                      final value = await openDialog();

                      setState(() => valueExpense = int.parse(value));
                      incrementCounter(valueExpense);
                    },
                    child: Icon(Icons.add),
                  ),
                ],
              )
          ),
        ],
      ),
    );
  }
}

class UniversityExpenses extends StatefulWidget {
  @override
  _UniversityExpenses createState() => _UniversityExpenses();
}

class _UniversityExpenses extends State<UniversityExpenses> {
  int _counter = 0;
  late TextEditingController controller;
  int valueExpense = 0;

  void incrementCounter(int value) async{
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('uniTotal') ?? 0) + value;
      prefs.setInt('uniTotal', _counter);
    });
  }

  void _loadCounter() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('uniTotal') ?? 0);
    });
  }

  @override
  void initState(){
    super.initState();
    controller = TextEditingController();
    _loadCounter();
  }

  @override
  void dispose(){
    controller.dispose();
    super.dispose();
  }

  void submit(){
    Navigator.of(context).pop(controller.text);

    controller.clear();
  }


  Future openDialog() => showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Add value expense'),
        content: TextField(
          autofocus: true,
          decoration: InputDecoration(hintText: 'Add the expense'),
          keyboardType: TextInputType.number,
          controller: controller,
        ),
        actions: [
          TextButton(
              onPressed: submit,
              child: Text('Done')
          )
        ],
      )
  );

  @override
  Widget build(BuildContext context){
    return Container(
      height: 50,
      margin: EdgeInsets.only(right: 200, left: 200),
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black26,
        ),
        borderRadius: BorderRadius.all(Radius.circular(20)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
              padding: EdgeInsets.all(10),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Icon(Icons.school),
                  Text('University',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 20,
                    ),
                  ),
                  Text('$_counter',
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 20,
                      )
                  ),
                  GestureDetector(
                    onTap: () async {
                      final value = await openDialog();

                      setState(() => valueExpense = int.parse(value));
                      incrementCounter(valueExpense);
                    },
                    child: Icon(Icons.add),
                  ),
                ],
              )
          ),
        ],
      ),
    );
  }
}

class HealthExpenses extends StatefulWidget {
  @override
  _HealthExpenses createState() => _HealthExpenses();
}

class _HealthExpenses extends State<HealthExpenses> {
  int _counter = 0;
  late TextEditingController controller;
  int valueExpense = 0;

  void incrementCounter(int value) async{
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('healthTotal') ?? 0) + value;
      prefs.setInt('healthTotal', _counter);
    });
  }

  void _loadCounter() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _counter = (prefs.getInt('healthTotal') ?? 0);
    });
  }

  @override
  void initState(){
    super.initState();
    controller = TextEditingController();
    _loadCounter();
  }

  @override
  void dispose(){
    controller.dispose();
    super.dispose();
  }

  void submit(){
    Navigator.of(context).pop(controller.text);

    controller.clear();
  }


  Future openDialog() => showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Add value expense'),
        content: TextField(
          autofocus: true,
          decoration: InputDecoration(hintText: 'Add the expense'),
          keyboardType: TextInputType.number,
          controller: controller,
        ),
        actions: [
          TextButton(
              onPressed: submit,
              child: Text('Done')
          )
        ],
      )
  );

  @override
  Widget build(BuildContext context){
    return Container(
      height: 50,
      margin: EdgeInsets.only(right: 200, left: 200),
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black26,
        ),
        borderRadius: BorderRadius.all(Radius.circular(20)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
              padding: EdgeInsets.all(10),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Icon(Icons.healing),
                  Text('Health',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 20,
                    ),
                  ),
                  Text('$_counter',
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 20,
                      )
                  ),
                  GestureDetector(
                    onTap: () async {
                      final value = await openDialog();

                      setState(() => valueExpense = int.parse(value));
                      incrementCounter(valueExpense);
                    },
                    child: Icon(Icons.add),
                  ),
                ],
              )
          ),
        ],
      ),
    );
  }
}

