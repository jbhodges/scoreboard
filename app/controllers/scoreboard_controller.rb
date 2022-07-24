class ScoreboardController < ApplicationController
  def home
  end

  def update_scoreboard
    hs = params[:home_scores]
    as = params[:visitor_scores]

      score_path = 'scores.json'
      File.open(score_path, "w") { |f| f.write params[:scoreboard].to_json }
      #Process.fork { system "sudo python3 test.py" }
    render json: { }

  end
end
