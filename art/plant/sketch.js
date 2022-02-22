let w = window.innerWidth > 0 ? window.innerWidth : screen.width;
let h = window.innerHeight > 0 ? window.innerHeight : screen.height;

let yPotTop = h - h / 3
let yPotBottom = h - h / 6

let xPotTop = Math.max(w / 4, w / 2 - 150)
let xPotTopOther = w - xPotTop

let xPotBottom = Math.max(w / 3, w / 2 - 100)
let xPotBottomOther = w - xPotBottom

let yStemTop = h / 6

function setup() {
  createCanvas(w, h);
}

function draw() {
  background(0);

  let t = millis()

  fill(255);

  drawPlant(t)
  drawPot(t)
}

function drawPlant(t) {
  push()
  stroke(255)
  drawStem(t)

  pop()
}

function drawStem(t) {
  push()
  strokeWeight(10)
  stroke("green")
  strokeCap(ROUND);


  let nPoints = 50
  let nWiggles = 2
  let stemHeight = yStemTop - yPotTop
  let wiggleSize = 10
  let wigglesPerSecond = 0.03

  let leafInds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 49]

  function calcY(i) {
    return yPotTop + i * stemHeight / nPoints 
  }

  function calcX(i) {
    return Math.sin(
      (i / nPoints + wigglesPerSecond * t / 1000)*2*Math.PI*nWiggles
    )*wiggleSize + w/2
  }

  let prev = 0
  let c = 0
  for (let i = 1; i<nPoints; i++) {

    let x0 = calcX(prev)
    let y0 = calcY(prev)
    let x1 = calcX(i)
    let y1 = calcY(i)

    if (leafInds.includes(i)) {
      drawLeaf(
        x1,
        y1,
        Math.atan(-(x1 - x0) / (y1 - y0)) + Math.PI * (c % 2),
        t
      )
      c++
    }
    line(x0, y0, x1, y1)

    prev = i
  }
  pop()
}

function drawLeaf(x, y, angle, t) {
  push()
  translate(x, y)
  rotate(angle)

  let leafLength = 50
  strokeWeight(0)
  fill("green")

  ellipse(leafLength / 2 + 2, 0, leafLength, 20)

  let nVeins = 10

  strokeWeight(1)
  stroke("brown")

  for (let i = 0; i < nVeins; i++) {
    push()
    translate(i / nVeins * leafLength, 0)
    let veinLength = i == (nVeins -1) ? 5 : 9

    rotate(Math.PI/4)
    line(0, 0, veinLength, 0)
    rotate(-2*Math.PI/4)
    line(0, 0, veinLength, 0)

    pop()
  }
  
  line(0, 0, leafLength - leafLength / 9, 0)

  pop()
}

function drawPot(t) {
  push()
  strokeWeight(10);
  strokeCap(ROUND);
  stroke("#d74426");
  fill("#e2725b")
  quad(
    xPotTop, 
    yPotTop,
    xPotTopOther, 
    yPotTop,
    xPotBottomOther,
    yPotBottom,
    xPotBottom,
    yPotBottom,
  )  


  strokeWeight(0);
  fill("#d74426")
  textSize(32)
  textAlign(CENTER, CENTER)
  text("for liv\n<3", w/2, (yPotTop - yPotBottom)/2 + yPotBottom)

  pop()
}