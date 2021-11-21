import React from 'react';
import './App.css';

class HelloWorld extends React.Component {
  render() {
    let DateTimeNow = new Date().toTimeString()
    return (
    <div>
      <h1>Hello world {this.props.myframe}</h1> <p>Now time = {DateTimeNow}</p>
    </div>)
  }
}



  // const todos = [
  //   {'id':1, 'title': 'Купить молоко', 'complited': false},
  //   {'id':2, 'title': 'Купить воды', 'complited': false},
  //   {'id':3, 'title': 'Купить мяса', 'complited': false},
  //   {'id':4, 'title': 'Купить рыбу', 'complited': false},
  //   {'id':5, 'title': 'Купить майонез', 'complited': false},
  //   {'id':6, 'title': 'Купить хлеб', 'complited': false},
  //   {'id':7, 'title': 'Купить масло', 'complited': false}
  // ]

  // return (
  //   <div className="App">
  //       <TodoList todos={todos} />
  //   </div>
  // );


export default HelloWorld;
