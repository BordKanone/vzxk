import React, {useState} from "react";

export default function App() {

    let [likes, setLikes] = useState(1)
    let [value, setValue] = useState()

    function increment(){
        setLikes(likes+1)
    }

    function decrement(){
        setLikes(likes-1)
    }

    return(

        <div className='App'>
                <h1>{likes}</h1>
                <h2>{value}</h2>
                <input type="text" value={value} onChange={event => setValue(event.target.value)}/>
                <button onClick={increment}>increment</button>
                <button onClick={decrement}>increment</button>
        </div>
    )
}
