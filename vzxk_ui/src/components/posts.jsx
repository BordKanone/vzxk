import React from "react";
import FormButton from "./ui/FormButton";

export default function PostItem(props) {
    return(
        <div className = 'post' >
            <div className="post__content">
                <strong>{props.number}. {props.post.title}</strong>
                <div>{props.post.body}</div>
            </div>
            <div className="post__btn">
                <FormButton onClick={()=> props.remove(props.post)}>Удалить</FormButton>
            </div>
        </div>
    )
}