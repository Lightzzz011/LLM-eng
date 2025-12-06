const response = await fetch("https://api.openai.com/v1/chat/completions",
                              { Method : "POST",
                                headers: { "Content-Type" : "application/json",
                                    "Authorization" : 'Bearer ${OPENAI_API_KEY}'
                                        },
                                        body : JSON.stringify({
                                            model : "gpt-4o",
                                            messages:[{role:"user",content:"Who is neyy"}]
                                        })
                              });
                              const data =await response.json();
                              console.log(data);