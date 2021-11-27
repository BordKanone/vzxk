import React from "react";
import FormButton from "./ui/FormButton/FormButton";

export default function PostItem(props) {
    return(
        <div className = 'post' >
            <div className="post__content">
                <strong>{props.number}. {props.post.first_name} {props.post.last_name}
                {props.post.three_name}</strong>
                <div>{props.post.about}</div>
            </div>
            <div className="post__btn">
                <FormButton onClick={()=> props.remove(props.post)}>Удалить</FormButton>
            </div>
        </div>
    )
}