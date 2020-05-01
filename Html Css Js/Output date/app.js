const showDate = (date = new Date()) => {
  const days = date.getDay();
  const months = date.getMonth();
  const years = date.getFullYear();
  return `${days}/${months}/${years}`;
};

console.log(showDate());
