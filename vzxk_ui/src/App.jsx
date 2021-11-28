import React, {useState, useEffect} from "react";
import PostList from "./components/PostList";
import PostForm from "./components/PostForm";
import PostFilter from "./components/PostFilter";
import CreateModal from "./components/ui/modal/CreateModal";
import FormButton from "./components/ui/FormButton/FormButton";
import './styles/App.css';
import { usePosts } from "./components/hooks/usePosts";
import PostService from "./API/PostService";
import QrCodeForm from "./components/qrcode/QrCodeForm";


export default function App(){
    const [posts, setPosts] = useState([])
    const [filter, setFilter] = useState({sort:'', query:''})
    const [modal, setModal] = useState(false)
    const getSortedandFilteredList = usePosts(posts, filter.sort, filter.query)
    const [isLoading, setIsLoading] = useState(false)
    
    useEffect(()=>{
        fetchPosts()
    }, [])

    async function fetchPosts() {
        setIsLoading(true)
        setTimeout( async()=>{
            const posts = await PostService.getAll();
            setPosts(posts)
            setIsLoading(false)
        },2000)
        
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
            <QrCodeForm/>
            {isLoading
            ? <h2>Идет загрузка...</h2>
            : <PostList remove={removePost} posts={getSortedandFilteredList} title='Список постов'/>}
        </div>
        )
} 