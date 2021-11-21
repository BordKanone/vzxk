import React from 'react';
// import axios from 'axios';

function PersonGet() {
    // const [people, setPeople] = useState([])

    // useEffect( ()=> {
    //     axios({
    //         method: 'GET',
    //         url: 'http://127.0.0.1:8000/customers'
    //     }).then(response=> {
    //         setPeople(response.data)
    //     })
    // }, [])


    return (
            <div className='peopleGet'>
                <div className='userCard'>
                    <div className='username'>
                        <p key='1' >Жунина</p>
                        <p key='1' >Анна</p>
                        <p key='1' >Денисовна</p>
                        <p className='about' key= '1'>Менеджер по работе с сушами</p>
                    </div>
                    <img className='avatar' src='/photo_2021-11-16_01-00-01.jpg'></img>
                </div>
            </div>
            )
}

export default PersonGet;