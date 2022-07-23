import React from "react";

export default function Gig({ list }) {
  let image_link;
  if (list.image == null) {
    image_link = "/images/business_wordpress_website.jpg";
  } else {
    image_link = list.image;
  }

  let base = "http://127.0.0.1:8000";
  // let rating = 10
  // let rate = Math. round(rating/2)

  return (
    <div className=" group ">
      <div className="group-hover:scale-105  transition transform ">
        <img src={`${base}${image_link}`}/>
      </div>
      <div>
        <p className="truncate px-1 py-1 text-sm cursor-pointer">{list.name}</p>
        <p className="truncate  px-1 py-1 font-bold cursor-pointer">
          {list.title}
        </p>
      </div>
      <div className="flex px-1 items-center opacity-0 group-hover:opacity-100">
        {/* <p className="font-bold text-sm">
            Rating: {rating}
        </p>
        <div className="flex px-1" >
            {[...Array(rate)].map(rate => <StarIcon className="rate fill-yellow-400 w-4 h-4"/>)}
        </div> */}
        {/* <p className=" pl-2 font-bold text-sm">{result.release_date}</p> */}
      </div>
    </div>
  );
}
