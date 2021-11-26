import React from "react";
import PostItem from "./posts";

export default function PostList(props) {
    return(
        <div>
            {props.posts.length !==0 
                ? <h1 style={{textAlign: 'center'}}>{props.title}</h1>
                : <h1 style={{textAlign: 'center'}}> Посты не найдены </h1>}
            
            {props.posts.map((post, index)=>
                 <PostItem remove={props.remove} number={index+1} post={post} key={post.id}/>
            )
            }
        </div>
    )
}