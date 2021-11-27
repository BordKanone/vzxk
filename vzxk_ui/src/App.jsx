import React, {useState, useMemo} from "react";
import PostList from "./components/PostList";
import PostForm from "./components/PostForm";
import PostFilter from "./components/PostFilter";
import CreateModal from "./components/ui/modal/CreateModal";
import FormButton from "./components/ui/FormButton/FormButton";
import './styles/App.css';
import axios from 'axios';
import { usePosts } from "./components/hooks/usePosts";


export default function App(){
    const [posts, setPosts] = useState([])
    const [filter, setFilter] = useState({sort:'', query:''})
    const [modal, setModal] = useState(false)
    const getSortedandFilteredList = usePosts(posts, filter.sort, filter.query)
    

    async function fetchPosts() {
        const response = await axios.get('http://127.0.0.1:8000/customers')
        setPosts(response.data)
    }

    const createPost = (newPost) => {
        setPosts([...posts, newPost])
        setModal(false)
    }

    const removePost = (post) =>{
        setPosts(posts.filter(p=> p.id !== post.id))
    }

    return(
        <div>

            <PostFilter filter={filter} setFilter = {setFilter}/>
            <FormButton onClick={fetchPosts}>GET</FormButton>
            <CreateModal visible={modal} setVisible={setModal}>
                <PostForm create = {createPost}/>
            </CreateModal>
            <FormButton style={{marginTop: '15px'}} onClick={()=>setModal(true)}>
                Создать пост
            </FormButton>
            <PostList remove={removePost} posts={getSortedandFilteredList} title='Список постов'/>
        </div>
        )
} 