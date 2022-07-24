Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"

  root             'scoreboard#home'
  post              'update_scoreboard'  => 'scoreboard#update_scoreboard'
end
