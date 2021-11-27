import React from "react";
import PostItem from './PostItem'
import {
    CSSTransition,
    TransitionGroup,
  } from 'react-transition-group';


export default function PostList(props) {
    return(
        <div>
            {props.posts.length !==0 
                ? <h1 style={{textAlign: 'center'}}>{props.title}</h1>
                : <h1 style={{textAlign: 'center'}}> Посты не найдены </h1>}

            <TransitionGroup>
                {props.posts.map((post, index)=>
                    <CSSTransition
                        key={post.id}
                        timeout={100}
                        classNames="post"
                        >
                            <PostItem remove={props.remove} number={index+1} post={post}/>
                    </CSSTransition>
                )}
            </TransitionGroup>
            
        </div>
    )
}