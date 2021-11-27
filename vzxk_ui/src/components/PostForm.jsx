import React, {useState} from "react";
import FormButton from "./ui/FormButton/FormButton";
import FormInput from "./ui/input/FormInput";


export default function PostForm({create}){
    const [post, setPost] = useState({title:'', body:''}) 

    const addNewPost = (e) => {
        e.preventDefault()
        const newPost = {
            ...post, id: Date.now()
        }
        create(newPost)
        setPost({title:'', body:''})
    }

        return(
            <form >
                <FormInput 
                    value={post.title} 
                    onChange={e => setPost({...post, title: e.target.value})}
                    type="text" 
                    placeholder='Название'
                    />
                <FormInput 
                    value={post.body}
                    onChange = {e => setPost({...post, body: e.target.value})} 
                    type="text" 
                    placeholder='Содержимое'
                    />
                <FormButton onClick={addNewPost} >Создать пост</FormButton>
            </form>
        )
    }