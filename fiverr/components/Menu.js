import React from 'react'
import Category from './Category'

export default function Menu() {
    let categories = ['Graphic $ Design', 
                    'Web Development',
                    'Mobile Development',
                    'Programming',
                     'Writing', 
                     'Music', 
                     'Video & Animation',
                      'Photography',
                       'Business', 
                       'Software', 
                       'Other'];
  return (
    <div className=" px-2 border-y-2 flex justify-between items-center  py-2">
       {categories.map(category => <Category  name={category}/>)} 
      </div>
  )
}
