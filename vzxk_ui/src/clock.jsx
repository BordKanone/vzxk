import React from "react";

function sayHello(props){
    return `${props} - say hello`
}

class Clock extends React.Component {
    constructor(props){
        super(props)
        this.state = {currentTime: (new Date()).toLocaleString()}}

        

    componentDidMount(){
        this.timerId=setInterval(() => {
            this.setState({currentTime: (new Date()).toLocaleString()})
        }, 1000);}  

    componentWillUnmount(){
        clearInterval(this.timerId)
    }
    render(){
        return(
            <div>{this.state.currentTime}</div>
            )} 
}

export default Clock;