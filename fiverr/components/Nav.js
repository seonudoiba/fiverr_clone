import React from "react";

export default function Nav() {
  return (
    <div>
      <nav className="nav navbar my-4 flex justify-around items-center">
        <div>
          <span className="text-4xl font-bold px-4">Starr</span>
        </div>
        <form className="w-1/2">
          <div className="relative mr-2 ml-1">
            <input
              type="search"
              id="default-search"
              className="block pl-10 w-full p-2 text-sm rounded-sm"
              placeholder="What service are you looking for today?"
              required=""/>
            <svg
              className="w-6 h-6 bg-grey-700 hover:bg-grey-500 absolute bottom-2 right-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </div>
        </form>
        <div className="icons nav navbar flex justify-between items-center">
          <svg
            className="w-6 h-6 m-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
            />
          </svg>
          <svg
            className="w-6 h-6 m-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
            />
          </svg>
          <svg
            className="w-6 h-6 m-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
            />
          </svg>
        </div>
        {/* // Profile Div */}

        <div className="flex items-center flex-wrap justify-end">
          <span className="m-4"> Orders</span>
          <span className="m-4"> Switch to Buying</span>
          <span className="mx-1"> Profile</span>
        </div>
      </nav>

      
    </div>
  );
}
