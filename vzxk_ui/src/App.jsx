import React, {useState, useMemo} from "react";
import PostList from "./components/PostList";
import PostForm from "./components/PostForm";
import FormSelect from "./components/ui/selected/FormSelect";
import FormInput from "./components/ui/input/FormInput";

export default function App(){
    let [posts, setPosts] = useState([])
    let [selectedSort, setSelectedSort] = useState('')
    let [searchQuery, setSearchQuery] = useState('')

    const sortedPostList = useMemo(()=>{
        console.log('use memo')
        if (selectedSort){
            return [...posts].sort( (a,b) => a[selectedSort].localeCompare(b[selectedSort]) ) 
        }
        else{
            return posts;
        }
    }, [selectedSort, posts])

    const getSortedandFilteredList = useMemo(()=>{
        return sortedPostList.filter(post => post.title.toLowerCase().includes(searchQuery))
    }, [searchQuery, sortedPostList])

    const createPost = (newPost) => {
        setPosts([...posts, newPost])
    }

    const removePost = (post) =>{
        setPosts(posts.filter(p=> p.id !== post.id))
    }
    
    const sortPosts = (sort)=>{
        setSelectedSort(sort)
        
    }

    return(
        <div>
            <FormInput
             value = {searchQuery}
             onChange = {e => setSearchQuery(e.target.value)}
             placeholder = 'Поиск' />
            <FormSelect
                value = {selectedSort}
                onChange = {sortPosts}
                defaultValue='Сортировка' options={[
                {value: 'title', name:'По названию'},
                {value: 'body', name:'По содержанию'}
            ]}/>
            <PostForm create = {createPost}/>
            <PostList remove={removePost} posts={getSortedandFilteredList} title='Список постов'/>
        </div>
        )
} 